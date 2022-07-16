import vk_api
import time
import telebot
from datetime import datetime


bot = telebot.TeleBot('5420997675:AAGsGYvu6ydVQr_QPOA9WrjsISD7mVAgbxo')


access_token="vk1.a.-snopOnAFEOAUx5_bIzIk_z5VHWiaNDzoPejaMfqImH69hTgREgxlnCq17DpUZH7aCZwLW1K4TzRNy50NBCPA5HHm95PLvSCnH3uSzLtPUir8IrxtIae5HrLBLrG0g1e-qF0-3TuIBsSnl8N81CzzEVnLOL2VJgIXvr-2ln3j8bfpbIZwiAENnWyyhLmhhFY"
session = vk_api.VkApi(token=access_token)
vk = session.get_api()


@bot.message_handler(commands=["start"])
def start(message):
    global w
    w = {470375497: False, 488240608: False, 527591313: False, 78326418: False, 395352962: False, 736873012: False}
    while True:
        time.sleep(5)
        get_online(458421518)


def get_online(id):
    q = session.method("friends.getOnline", {'user_id': id})
    q1 = session.method("friends.search", {'user_id': id, 'count': 175})['items']
    for i in w.keys():
        if w[i] and i not in q:
            t = datetime.now()
            current_time = t.strftime("%H:%M:%S")
            for j in q1:
                if i == j['id']:
                    name = j['first_name'] + " " + j['last_name']
                    bot.send_message(1100573072, f"{name} вышел из сети {current_time}")
                    w[i] = False
    for i in w.keys():
        if not w[i]:
            if i in q:
                t = datetime.now()
                current_time = t.strftime("%H:%M:%S")
                for j in q1:
                    if i == j['id']:
                        w[i] = True
                        name = j['first_name'] + " " + j['last_name']
                        bot.send_message(1100573072, f"{name} в сети {current_time}")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

