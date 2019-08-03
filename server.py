from flask import Flask, request
import json
from flask import make_response

app = Flask(__name__)
 
@app.route('/',methods=['POST'])
def hello_world():
    import text
    import NER.ner_tagging
    text1 = request.get_data()
    list_result = NER.ner_tagging.get_main(text1)
    return json.dumps(list_result,ensure_ascii=False)


@app.route('/')
def hello_world1():
    import text
    import LGQ_code.test
    r = request.args.get('text')

    
    list_result = LGQ_code.test.mycode(r)

    rst = make_response(list_result)
    rst.headers['Access-Control-Allow-Origin'] = '*'

    return rst


    # rst = make_response(list_result)
    # rst.headers['Access-Control-Allow-Origin'] = '*'

    return list_result

    return json.dumps(list_result,ensure_ascii=False)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8081, debug=True)


