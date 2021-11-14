from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request

app = Flask(__name__)


def func(smth):
    if (smth) == 'джинсы':
        return list(['пастеризовать', 'брюки', 'шорты', 'пиджак', 'джинсовый'])
    else:
        return list(['-', '-', '-', '-', '-'])


def func2(smth):
    if smth == 'капри для подростков':
        return list(['капри под пиджак', 'капри olbe', 'капри жля плавания', 'капри осенние', 'брюки капри большой размер', 'капри кроссовки', 'капри reebok'])
    if smth == 'капри и блузка летние':
        return list(['женские капри вельвет',
 'капри мальчику',
 'капри из льна',
 'капри для спорта с высокой посадкой',
 'портьера капри канвас',
 'купить капри женские',
 'ремешок для apple watch 44 капри blue'])
    if smth == 'капри для девочки':
        return list(['капри женские 56 раз',
 'капри глазные',
 'солнце капри духи',
 'капри хлопок беларусь',
 'капри для фитнеса женские',
 'капри сетка',
 'капри спаленка'])
    if smth == 'капри женские найк':
        return list(['капри офис',
 'актуальный костюм меланж с брюками-капри - stīlish',
 'полосатые бриджи капри свободные',
 'капри на девочку оранжевые',
 'капри сетка',
 'комплекст капри и топ спортивный',
 'костюм с капри женские для пляжа'])
    if smth == 'капри размера 64':
        return list([ 'капри из плащевки',
 'свободные капри короткие брюки',
 'капри тёплые',
 'капри с широким поясом',
 'летние капри большой размер женские',
 'женские капри для дома и отдыха 52-58 размеры масло облегающего силуэта с небольшими разрезами по бокам с бан...',
 'капри с резинкой'])
    else:
        return list(['-', '-', '-', '-', '-', '-', '-'])


@app.route('/', methods=['POST', 'GET'])
def input():
    qqq = ['капри для подростков', 'джинсы', 'капри и блузка летние', 'капри для девочки','капри из плащевки', 'капри офис']
    return render_template("input.html", qqq=qqq)


@app.route('/output', methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        user_input = request.form
        # output = func(user_input['data'])
        # output = func(user_input['data'])
        big_output = {'Similar tags': func(user_input['data']),
                      'Clarifying tags': func2(user_input['data'])}
        # output = give_tags(user_input['data'])
        return render_template("output.html", tags=big_output, request=user_input['data'])


if __name__ == '__main__':
    app.run(debug=True)
