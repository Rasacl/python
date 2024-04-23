from googletrans import Translator


def has_chinese(text):
    """Check if the text contains Chinese characters."""
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False


def translate_markdown(input_file, output_file):
    # 创建谷歌翻译器对象
    translator = Translator()

    # 读取Markdown文件内容并按段落分割
    with open(input_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
        paragraphs = markdown_content.split('\n\n')  # 根据空行分割段落

    # 逐段翻译并重建Markdown内容
    translated_paragraphs = []
    code_block = False  # 标记是否处于代码块中
    for paragraph in paragraphs:
        # 检查是否处于代码块中
        if paragraph.startswith('```') and not code_block:
            code_block = True
            translated_paragraphs.append(paragraph)
            continue
        elif paragraph.startswith('```') and code_block:
            code_block = False
            translated_paragraphs.append(paragraph)
            continue

        # 检查是否包含图片引用
        if '![' in paragraph and ']' in paragraph and '(' in paragraph and ')' in paragraph:
            translated_paragraphs.append(paragraph)
            continue  # 跳过包含图片引用的段落

        if has_chinese(paragraph) and not code_block:  # 在非代码块中的含中文段落才进行翻译
            translated_paragraph = translator.translate(paragraph, dest='en', src='auto').text
            translated_paragraphs.append(translated_paragraph)
        else:
            translated_paragraphs.append(paragraph)

    # 将翻译后的内容写入输出文件
    translated_content = '\n\n'.join(translated_paragraphs)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_content)


# 指定输入和输出文件路径
input_file_path = 'input.md'
output_file_path = 'output_file.md'

# 调用翻译函数
translate_markdown(input_file_path, output_file_path)
