import os

class Translation(object):

  FROM_MSG = "<b><u>SET FROM CHANNEL USERNAME</b></u>\n<b>Enter From Channel Username</b>\n<code>eg: @username</code>\n/cancel <code>- Cancel this process</code>"
  TO_MSG = "<b><u>SET TO CHANNEL ID</b></u>\n<b>Enter To Channel id</b>\n<code>eg: -100xxxxxxxxxx</code>\n/cancel <code>- Cancel this process</code>"
  SKIP_MSG = "<b><u>SET FILE SKIPING NUMBER</b></u>\n<b>Skip the file as much as you enter the number and the rest of the file will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 file skiped\n You enter 5 = 5 file skiped</code>\n/cancel <code>- Cancel this process</code>"
  LIMIT_MSG = "<b><u>SET FILE FORWARD LIMIT</u></b>\n<b>Heroku Daily Limit</b> : <code>23000</code>\n<b>Default Limit</b> : <code>0</code>"
  CANCEL = "<b>Process Cancelled Succefully\nEnter /run Again</b>"
  USERNAME = "<b>Send Username with @</b>\n<code>eg: @Username</code>\n<b>Enter /run Again</b>"
  INVALID_CHANNELID = "<b>Send channel id with -100</b>\n<code>eg: -100xxxxxxxxxx</code>\n<b>Enter /run Again</b>"
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the file Click the Yes button only after checking the following</code>

<i>° Must be a user join in From channel check that status</i>
<i>User join this channel : <b>{}</b></i>
<b><u>Note</u></b> : <i>Admin permission is not mandatory</i>
<i>° Admin permission is mandatory for the bot on the To channel check that status</i>
<b><u>Note</u></b> : <i>There is no requirement for a user to join the To channel</i>

<b>If the above is checked then the yes button can be clicked</b>"""
