import pars
import message
import vk_api

fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))

vk_session = vk_api.VkApi( token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
"""
хуй соси если не наешл этот писька комит 

а Александр молодец

<<<<<<< HEAD
Хорошо сосет хуи Олег
=======
Хорошо сосет хуи 
Саня парсер верни
>>>>>>> 98a0a3dc7ed0a91ba3e0de629ed8eb52ea532777
"""
message.Mess(fuck, vk_session)
