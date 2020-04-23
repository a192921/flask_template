## flask template-render

### 檔案路徑位置:
![](https://i.imgur.com/dUHwlR1.png)
![](https://i.imgur.com/3J96xHa.png)
```pythons
from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
directory = os.getcwd()


@app.route('/')
def index():
    return render_template('index.html')
    # return directory


if __name__ == '__main__':
    app.debug = True
    app.run()

```
#### 輸出結果:
![](https://i.imgur.com/v9U78s9.png)

