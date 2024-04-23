---
order: 50
---

# Blueprint node development

## Create

To develop a blueprint node, you need to inherit from the type of `Thing.bluprint.baseNode`, or inherit the subclasses from other` BaseNode`, such as: `Base3dnode`, etc. The simplest blueprint node is as follows:

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

If there is a `callback` recovery in the` Outputs`, you need to start a new execution chain in the event callback, such as: `this.run ('click', outputs)`.

## stop

When the blueprint stops, the `OnStop` method of all nodes is called.The global variables used in the `Onexecute` method in the` OnStop`.For example, the method and other methods such as the `ADDEVENTLISTENENER`, `SetInterval` and other methods are used in the` Onexecute` method. You need to call the corresponding `RemoveeventListener` and` Clearinterval.

## register

After developing the blueprint node, you need to register to make the blueprint editor and `Thingjs` run when running:

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

## Precautions

## code specification

There are some code specifications in the development of the blueprint node and do not serve as compulsory requirements. However, the code should be written according to these specifications during development:

-When the name of the blueprint nodes should start with `bp`;
-If of the blueprint node, if it is a method of a certain class, it is generally named after the name+method of this class, such as: `BPOBJECTSETPOSITION,`BPCameraflyto, and some global methods directly start with verbs, such as: `bpcreatebox`, etc.;
-If the blueprint node, there is only one execution connection point. In order to simplify, the `name` at this connection point is called` exec` (the blueprint editor will only display one arrow);

## sample

Below is a complete example, used to achieve a delayed blueprint node

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
