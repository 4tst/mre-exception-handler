# MRE for [Can not capture the child class of "Exception" in app.exception_handler globally](https://github.com/fastapi/fastapi/discussions/7008)

## steps

1. `git clone https://github.com/4tst/mre-exception-handler.git`
2. `python server.py`
3. open `./frontend/index.html` in browser and watch `network tab in devtools`

### test 1
1. comment `@app.exception_handler(ValueError)`
2. refresh `index.html` and observe devtools, the api responses 200, but with CORS Error

### test 2
1. uncomment `@app.exception_handler(ValueError)`
2. refresh `index.html` and observe devtools, the api responses as expected


