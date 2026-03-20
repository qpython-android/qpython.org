# WakeLock API

控制设备唤醒锁以保持 CPU 或屏幕开启。

## Wake Lock 类型

QSL4A 提供不同类型的唤醒锁：

| 类型 | 描述 |
|------|-------------|
| Full | CPU 开启，屏幕亮，键盘亮 |
| Partial | 仅 CPU 开启 |
| Bright | CPU 开启，屏幕亮 |
| Dim | CPU 开启，屏幕暗 |

## Wake Lock 方法

### wakeLockAcquireFull() *ASL4A*
获取完整唤醒锁（CPU 开启，屏幕亮，键盘亮）。

```python
wakeLockAcquireFull()
```

### wakeLockAcquirePartial() *ASL4A*
获取部分唤醒锁（仅 CPU 开启）。

```python
wakeLockAcquirePartial()
```

### wakeLockAcquireBright() *ASL4A*
获取明亮唤醒锁（CPU 开启，屏幕亮）。

```python
wakeLockAcquireBright()
```

### wakeLockAcquireDim() *ASL4A*
获取暗淡唤醒锁（CPU 开启，屏幕暗）。

```python
wakeLockAcquireDim()
```

### wakeLockRelease() *ASL4A*
释放唤醒锁。

```python
wakeLockRelease()
```

## 使用示例

```python
import androidhelper
import time

droid = androidhelper.Android()

# 获取完整唤醒锁
droid.wakeLockAcquireFull()

# 在保持屏幕开启时执行重要工作
print("Screen will stay on")
time.sleep(10)

# 完成后释放
droid.wakeLockRelease()

# 或使用部分锁进行后台任务
droid.wakeLockAcquirePartial()
# 即使屏幕关闭，CPU 仍保持开启
time.sleep(30)
droid.wakeLockRelease()
```

**注意：** 记住在不需要时释放唤醒锁以节省电池。
