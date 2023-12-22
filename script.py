# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect()

#+
d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND").click()
d.click(0.325, 0.75)
#创建对号
d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND").click()
#搜索按钮
d(resourceId="org.totschnig.myexpenses.debug:id/SEARCH_COMMAND").click()
#amount
d.xpath('//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
#输入框
d(resourceId="org.totschnig.myexpenses.debug:id/amount1").click()
d.click(0.508, 0.808)
#ok
d(resourceId="android:id/button1").click()
#右上角仨点
d(description="More options").click()
#export and reset
d.xpath('//android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
#export
d(resourceId="android:id/button1").click()