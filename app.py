#encoding:utf-8
from flask import Flask
from urllib import urlopen
import datetime,base64,random,re
def get_qcode_img():
    data=base64.b64encode("QT；%d；%s"%(random.randint(105000,108000),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    data=re.findall('<img src="(.+)" id="qrcode_plugins_img" class="qrcode_plugins_img" style="background: r',urlopen("https://cli.im/api/qrcode/code?text=%s&mhid=5EvBXw6/m88hMHcrKtxdMa8"%data).read())[0]
    return data

app = Flask(__name__)
@app.route('/qtlibrary/')
def hello():
    baidu_tongji='''
    <script>
    var _hmt = _hmt || [];
    (function() {
          var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?30f28cc0dcaaac6c58943bfea5bc638e";
              var s = document.getElementsByTagName("script")[0]; 
                s.parentNode.insertBefore(hm, s);
    })();
    </script>
    '''
    return "<img src='%s'>\n\n%s"%(get_qcode_img(),baidu_tongji)


if __name__ == '__main__':
    app.run()
