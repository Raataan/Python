#python3
# -*- coding: utf-8 -*-
#code like shit，just testing and personal use

import requests

header = {
    'Host': 'www.sojump.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3,',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://www.sojump.com/jq/5083814.aspx',
    'Content-Length': '149',
    'Cookie': '.ASPXANONYMOUS=Lyje67TM0AEkAAAAZmUxZjg2ZDktMGQxMy00N2FkLTk5MTktMTgzZTczMzI1MmQ4vetgQ0kJRBRF_ryF5iUJakL6RC01; ASP.NET_SessionId=ezddzrjpltnx1via0l2gdjz4; CNZZDATA4478442=cnzz_eid%3D601949447-1432471183-%26ntime%3D1432471183; LastActivityJoin=5083814,204649401; bdshare_firstime=1432473304766',
    'X-Forwarded-For': '8.8.8.8',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

header2 = {
    'Host': 'www.sojump.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.sojump.com/jq/5083814.aspx',
    'Cookie': '.ASPXANONYMOUS=Lyje67TM0AEkAAAAZmUxZjg2ZDktMGQxMy00N2FkLTk5MTktMTgzZTczMzI1MmQ4vetgQ0kJRBRF_ryF5iUJakL6RC01; ASP.NET_SessionId=ezddzrjpltnx1via0l2gdjz4; CNZZDATA4478442=cnzz_eid%3D601949447-1432471183-%26ntime%3D1432471183; LastActivityJoin=5083814,204649401; bdshare_firstime=1432473304766',
    'X-Forwarded-For': '8.8.8.8',
    'Connection': 'keep-alive'
}

thedata = {'submitdata': '1$1}2$3}3$1}4$2}5$4}6$4}7$1|2|3|4}8$3}9$3}10$1|3|4|6}11$3}12$3}13$3}14$4'}

for no in range(1,1000):
    #url = 'http://www.sojump.com/jq/5083814.aspx/handler/processjq.ashx?submittype=1&curID=5083814&t=1432473130531&starttime=2015/5/24 21:11:01&rn=138341469'
    url = 'http://www.sojump.com/handler/processjq.ashx?submittype=1&curID=5083814&t=1432473130531&starttime=2015/5/24 21:11:01&rn=138341469'

    url2 = 'http://www.sojump.com/jq/5083814.aspx/wjx/join/complete.aspx?q=5083814&JoinID=204649401&s=&ge=1'
    #url2 = 'http://www.sojump.com/handler/processjq.ashx?/wjx/join/complete.aspx?q=5083814&JoinID=204649401&s=&ge=1'

    r2 = requests.get(url2, headers = header2)
    r = requests.post(url, headers = header,data = thedata)


    print(r.text)
    print(r2.text)
