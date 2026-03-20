# 信号强度 API

监控蜂窝和无线信号强度。

## 信号强度方法

### startTrackingSignalStrengths() *ASL4A*
开始跟踪信号强度变化。生成 'signal_strengths' 事件。

```python
startTrackingSignalStrengths()
```

### stopTrackingSignalStrengths() *ASL4A*
停止跟踪信号强度。

```python
stopTrackingSignalStrengths()
```

### readSignalStrengths() *ASL4A*
读取当前信号强度。

```python
readSignalStrengths()
```

**返回：** 包含信号强度数据的 Bundle

### getTelephoneSignalStrengthLevel() *ASL4A*
获取电话信号强度等级（0-4）。

```python
getTelephoneSignalStrengthLevel()
```

**返回：** 整数等级（0=无，1=差，2=一般，3=好，4=优秀）

### getTelephoneSignalStrengthDetail() *ASL4A*
获取详细的电话信号强度信息。

```python
getTelephoneSignalStrengthDetail()
```

**返回：** 包含详细信号信息的字符串

## 使用示例

```python
import androidhelper
import time

droid = androidhelper.Android()

# 开始跟踪信号强度
droid.startTrackingSignalStrengths()

# 等待信号更新
time.sleep(5)

# 读取当前信号强度
signal = droid.readSignalStrengths().result
print(f"Signal: {signal}")

# 直接获取等级
level = droid.getTelephoneSignalStrengthLevel().result
print(f"Signal level: {level}/4")

droid.stopTrackingSignalStrengths()
```
