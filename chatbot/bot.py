from threading import Thread
from chatbot.fb_graph_api import send_api
from chatbot.bot_flow import Flow

class Bot(Thread):
	def __init__(self , page_access_token):
		Thread.__init__(self)
		self.__page_access_token = page_access_token

	# TRAITE LES DONNEES DE LA REQUETTE POST
	# CREE UN OBJET message
	def run(self , request):
		message = Message(request)
		Flow().start_flow(message)

	def get_page_access_token(self):
		return self.__page_access_token



class Message():
	def __init__(self , request_content):
		self.__request_content = request_content
		self.__sender_id = self.__request_content["entry"][0]["messaging"][0]["sender"]["id"]
		self.__message_type = list(self.__request_content["entry"][0]["messaging"][0].keys())
		self.__message_type = self.__message_type[len(self.__message_type) - 1]

		if  self.__message_type == "message":
			self.__message_type = list(self.__request_content["entry"][0]["messaging"][0]["message"].keys())
			self.__message_type = self.__message_type[len(self.__message_type) - 1]
			if self.__message_type == "attachments":
				pass
			elif self.__message_type == "text":
				self.__message_text_content = self.__request_content["entry"][0]["messaging"][0]["message"]["text"]	
			elif self.__message_type == "quick_reply":
				self.__message_text_content = self.__request_content["entry"][0]["messaging"][0]["message"]["text"]
				self.__message_payload = self.__request_content["entry"][0]["messaging"][0]["message"]["quick_reply"]["payload"]
		elif self.__message_type == "postback":
			self.__message_text_content = self.__request_content["entry"][0]["messaging"][0]["postback"]["title"]
			self.__message_payload = self.__request_content["entry"][0]["messaging"][0]["postback"]["payload"]

	def get_sender_id(self):
		return self.__sender_id

	def get_message_type(self):
		return self.__message_type

	def get_message_text_content(self):
		return self.__message_text_content

	def get_message_payload(self):
		if self.get_message_type() == "text":
			return None
		else:
			return self.__message_payload
			