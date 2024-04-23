---
order: 50
---

# 蓝图节点开发

## 创建

开发一个蓝图节点，需要继承自`THING.BLUEPRINT.BaseNode`类型，或继承自其他`BaseNode`的子类，如：`Base3DNode`等，一个最简单的蓝图节点如下：

```js
class BPTest extends BaseNode {
  static config = {}
  onExecute(data, inputs, outputs) {}
  onStop() {}
}
THING.BLUEPRINT.Utils.registerNode(BPTest)
```

你可以创建一个`js`文件来编写这个蓝图节点，也可以使用编辑器的向导来（开发菜单下的创建蓝图节点）帮你创建一个基础的蓝图节点：

![wizard](./images/bp-wizard.png '创建蓝图节点向导')

## 配置

蓝图节点的输入输出连接点，是靠`config`属性进行配置的，`config`属性是一个`json`格式的数据，包括`name`、`inputs`、`outputs`等。蓝图编辑器会根据这个配置在蓝图中生成节点，另外在节点内的`onExecute`方法中，也会使用这个配置数据。

> 注意：`config`中的`name`字段是蓝图节点的名称，此名称目前不可以重复。

### 连接点

`config`中的`inputs`/`outputs`字段，表示蓝图节点的输入/输出连接点。每个连接点包含下面一些字段：

- `name`: 连接点的名称，要求 `inputs/outputs` 内唯一。
- `type`: 连接点的数据类型，有动作类型和数值类型两种。
  - **动作类型**的连接点，会被调用，在`inputs`中代表执行方法；在`outputs`中代表执行下一步或事件的回调。动作类型目前有**执行**（`exec`） 和**回调**（`callback`）。
  - **数值类型**的连接点，只传数据，在`inputs`中代表`onExecute`执行时所需要的参数，在`outputs`中代表返回值。数值类型有`string` 、`boolean`、`number`、`select`、`vector3`、`vector2`、`any`、`color`、`array`、`object`等。
- `value`：连接点的默认值。
- `unit`： 数据单位

## 执行

蓝图节点中任何一个动作连接点被执行时，都会调用蓝图节点的`onExecute`方法，在`onExecute`方法中，可以通过`inputs`属性获取这个连接到这个节点的数据，以及通过和`outputs`属性返回数据给下一个节点，如：

```js
onExecute(data, inputs, outputs) {
	let num1 = inputs['num1'];
	let num2 = inputs['num2'];
	outputs['result'] = num1 + num2;
	......
}
```

如果`outputs`中有`callback`回调，则需要在事件的回调中，启动一个新执行链，如：`this.run('click', outputs)`。

## 停止

当蓝图停止运行后，会调用所有节点的`onStop`方法。应该在`onStop`中回收`onExecute`方法中使用的全局变量。比如在`onExecute`方法中使用了`addEventListener`、`setInterval`等方法，需要在`onStop`中调用相应的`removeEventListener`、`clearInterval`将其清空。

## 注册

开发完蓝图节点后，需要进行注册，才能够让蓝图编辑器以及`ThingJS`运行时使用：

```js
THING.BLUEPRINT.Utils.registerNode(BPNode)
```

还有注册右键菜单的位置……

## 国际化

## 样式

图标设置：节点前添加`@icon`注释

> 注意：图标路径相对于`bpnodes`文件夹

颜色设置：节点前添加`@headerColor`、`@bodyColor`注释

> 注意：`headerColor`、`bodyColor`需同时设置

```javascript
/**
 * 蓝图节点：机柜
 * @icon './images/my-bp-02.png'
 * @headerColor '#ff0000'
 * @bodyColor 'rgba(100, 200, 0, 0.9)'
 */
export class BPCabinet extends BPBaseCabinetNode {}
```

## 注意事项

## 代码规范

蓝图节点的开发中有一些代码规范，不作为强制要求，但在开发时应尽量按照这些规范编写代码：

- 蓝图节点类名要以`BP`开头；
- 蓝图节点的如果是某一个类的方法，一般以这个类的名字+方法的来命名，如：`BPObjectSetPosition`、`BPCameraFlyTo`，而一些全局方法直接以动词开头，如：`BPCreateBox`等；
- 如果蓝图节点只有一个执行的连接点，为了简化，一般这个连接点的`name`就叫`exec`（蓝图编辑器会只显示一个箭头）；

## 示例

下面是一个完整的实例，用于实现一个延时的蓝图节点

```javascript
class BPDelay extends BaseNode {
  static config = {
    name: 'delay',
    inputs: [
      {
        name: 'exec',
        type: 'exec'
      },
      {
        name: 'time',
        type: 'number',
        value: 1000,
        unit: 'ms'
      }
    ],
    outputs: [
      {
        name: 'trigger',
        type: 'callback'
      }
    ]
  }

  constructor() {
    super()
    this.timer = null
  }

  onExecute(data, inputs, outputs) {
    let delayTime = inputs['time']
    this.timer = setTimeout(() => {
      this.run('trigger', outputs)
    }, delayTime)
  }

  onStop() {
    clearTimeout(this.timer)
  }
}
THING.BLUEPRINT.Utils.registerNode(BPDelay)
```
