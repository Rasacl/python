import asyncio
import aiohttp
import pandas as pd

# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}

max_page = 500
semaphore = asyncio.Semaphore(6)


async def fetch_data(session, page):
    async with semaphore:
        url = f'https://ybj.hainan.gov.cn/tps-local/local/web/std/queryService/queryMcsPubRsltPage?current={page}&size=50'
        try:
            async with session.get(url, headers=headers) as response:
                data = await response.json()
                datas = data['data']['records']
                print(f'正在爬取第{page}页数据', len(datas))
                return datas
        except Exception as e:
            print('抛出异常', e)
            return []


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, page) for page in range(1, max_page + 1)]
        all_data = await asyncio.gather(*tasks)
        all_data = [item for sublist in all_data for item in sublist]
        chunk_df = pd.DataFrame(all_data)
        chunk_df = chunk_df[
            ['mcsCode', 'mcsName', 'prodentpName', 'mcsRegno', 'mcsSpec', 'mcsMatl', 'pubonlnPric']
        ]
        chunk_df.columns = ['耗材统一编码', '耗材名称', '生产企业', '注册证编号', '规格', '材质', '挂网价格']
        chunk_df.to_excel('海南耗材集采_500.xlsx', index=False)
        print('数据爬取完成并写入表格' + f'{len(all_data)}')


asyncio.run(main())
