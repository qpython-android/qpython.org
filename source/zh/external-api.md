# QPython 开放 API

QPython 有一个开放的 activity，允许您从外部运行 qpython。

MPyAPI 的定义如下：

```python

    <activity
        android:name="org.qpython.qpylib.MPyApi"
        android:label="@string/qpy_run_with_share"
        android:screenOrientation="user"
        android:configChanges="orientation|keyboardHidden"
        android:exported="true">
        <intent-filter>
            <action android:name="org.qpython.qpylib.action.MPyApi" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
        <intent-filter>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="http" />
            <data android:scheme="https" />
        </intent-filter>
        <intent-filter>
            <action android:name="android.intent.action.SEND"/>
            <category android:name="android.intent.category.DEFAULT"/>
            <data android:mimeType="text/plain"/>
        </intent-filter>
        <intent-filter>
            <action android:name="android.intent.action.SEND"/>
            <category android:name="android.intent.category.DEFAULT"/>
            <data android:mimeType="image/*"/>
        </intent-filter>
    </activity>

```

**因此，借助它，您可以：**

## 将内容分享到 QPython 的脚本

您可以在某个应用中选择一些内容，然后分享到 qpython 的脚本，之后您可以使用 **sys.argv[2]** 处理这些内容

[在 YouTube 上观看演示视频](https://www.youtube.com/watch?v=2Y50Yir8TWg)

## 从您自己的应用程序运行 QPython 的脚本

您可以通过调用此 activity 在您的应用程序中调用 QPython 来运行某些脚本或 Python 代码，示例如下：

```python

// 展示如何调用 qpython API 的代码示例
String extPlgPlusName = "org.qpython.qpy";          // QPython 包名
Intent intent = new Intent();
intent.setClassName(extPlgPlusName, "org.qpython.qpylib.MPyApi");
intent.setAction(extPlgPlusName + ".action.MPyApi");

Bundle mBundle = new Bundle();
mBundle.putString("app", "myappid");
mBundle.putString("act", "onPyApi");
mBundle.putString("flag", "onQPyExec"); // 您在上下文中可能使用的任意字符串标志
mBundle.putString("param", "");         // 您在上下文中可能使用的参数字符串

/*
* 我们将运行的 Python 代码
*/
String code = "import androidhelper\n" +
            "droid = androidhelper.Android()\n" +
            "line = droid.dialogGetInput()\n" +
            "s = 'Hello %s' % line.result\n" +
            "droid.makeToast(s)\n"

mBundle.putString("pycode", code);
intent.putExtras(mBundle);
startActivityForResult(intent, SCRIPT_EXEC_PY);
...

// 您可以在 onActivityResult 中处理 qpython 调用结果
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == SCRIPT_EXEC_PY) {
        if (data!=null) {
            Bundle bundle = data.getExtras();
            String flag = bundle.getString("flag");
            String param = bundle.getString("param");
            String result = bundle.getString("result"); // 您的 Pycode 生成的结果
            Toast.makeText(this, "onQPyExec: return ("+result+")", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "onQPyExec: data is null", Toast.LENGTH_SHORT).show();

        }
    }
}

```

[从 github 检出一个完整项目](https://github.com/qpython-android/app-call-qpython-api)

还有一个生产应用程序 - [面向 Tasker 的 QPython 插件](https://play.google.com/store/apps/details?id=com.qpython.tasker2)
