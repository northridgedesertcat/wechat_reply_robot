from wxauto import WeChat
import wxcontrol
import conf




if __name__=="__main__":
    wx = WeChat()
    wxcontrol.start_respond(wx,conf.user_list,conf.type,conf.think,conf.api,conf.jole,conf.history)
