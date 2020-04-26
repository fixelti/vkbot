import pars
import message
import vk_api

fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))

vk_session = vk_api.VkApi( token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
"""
хуй соси если не наешл этот писька комит 

а Александр молодец

Хорошо сосет хуи Олег
"""
message.Mess(fuck, vk_session)
