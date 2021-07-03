from chatbot.fb_graph_api import send_api
from chatbot import bot_actions

##############################################
#                DECISIONS PATHS             #
##############################################
class Flow():
	def start_flow(self , message):
		# MET UN VU ET UN ACTION "En train d'écrire"
		bot_actions.seen(message.get_sender_id())
		bot_actions.typing_on(message.get_sender_id())

		# GERE LES MESSAGES NORMAUX (SANS EMOJIS)
		if message.get_message_type() == "text":
			pass

		# GERE LES PIECES JOINTES (EMOJI , IMAGES , ...)
		elif message.get_message_type() == "attachments":
			pass

		# GERE LES REPONSES RAPIDES
		elif message.get_message_type() == "quick_reply":
			pass

		# GERE LES MESSAGES POSTBACK (BOUTONS , BOUTONS DU MENU FIXE)
		elif message.get_message_type() == "postback":
			pass

