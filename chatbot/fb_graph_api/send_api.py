#coding:utf-8
import requests
from requests_toolbelt import MultipartEncoder
import magic
import os

class SendApi():
	def __init__(self , page_access_token):
		self.__api_url = "https://graph.facebook.com/v11.0/me/messages"
		self.__page_access_token = page_access_token
		self.__graph_version = "11.0"

	def get_api_url(self):
		return self.__api_url

	def get_access_token(self):
		return self.__page_access_token

	def get_graph_version(self):
		return self.__graph_version

	def send_text_message(self , messaging_type , recipient_id , message):
		if messaging_type == "RESPONSE":
			request_body = {
								"messaging_type": messaging_type,
								"recipient": {
									"id": recipient_id
								},
								"message": {
									"text": message
								}
							}										   		

			return requests.post(self.get_api_url() , params={"access_token":self.get_access_token()} , json=request_body).json()

	def __send_attachment_message(self , attachment_type , attachment_url , recipient_id):
		request_body = {
							"recipient": {
								"id": recipient_id
							},
							"message": {
								"attachment": {
									"type": attachment_type,
									"payload": {
										"url": attachment_url,
										"is_reusable": "true"
									}
								}
							}
						}
		
		return requests.post(self.get_api_url() , params={"access_token":self.get_access_token()} , json=request_body).json()

	def send_image_attachment(self , attachment_url , recipient_id):
		return self.__send_attachment_message("image" , attachment_url , recipient_id).json()

	def send_video_attachment(self , attachment_url , recipient_id):
		return self.__send_attachment_message("video" , attachment_url , recipient_id).json()

	def send_audio_attachment(self , attachment_url , recipient_id):
		return self.__send_attachment_message("audio" , attachment_url , recipient_id).json()

	def send_file_attachment(self , attachment_url , recipient_id):
		return self.__send_attachment_message("file" , attachment_url , recipient_id).json()

	# elements must be in a list
	def send_generic_message(self , elements , recipient_id):
		request_body = {
							"recipient": 
							{
								"id": recipient_id
							},
							"message": 
							{
								"attachment": 
								{
									"type": "template",
									"payload": 
									{
										"template_type": "generic",
										"image_aspect_ratio" : "square",
										"elements": 
										elements
									}
								}
							}
						}
		
		return requests.post(self.get_api_url() , params={"access_token":self.get_access_token()} , json=request_body).json()

	def __send_sender_actions(self , sender_action , recipient_id):
		request_body = {
  							"recipient":{
    										"id":recipient_id
  										},
  							"sender_action":sender_action
					   }
		
		return requests.post(self.get_api_url() , params={"access_token":self.get_access_token()} , json=request_body).json()

	def mark_seen_message(self , recipient_id):
		return self.__send_sender_actions("mark_seen" , recipient_id)

	def typing_on_message(self , recipient_id):
		return self.__send_sender_actions("typing_on" , recipient_id)

	def typing_off_message(self , recipient_id):
		return self.__send_sender_actions("typing_off" , recipient_id)

	def send_quick_replies(self , messaging_type , message , quick_replies , recipient_id):
		request_body = {
							"recipient": {
								"id": recipient_id
							},
							"messaging_type": messaging_type,
							"message": {
								"text": message,
								"quick_replies": 
								quick_replies
							}
						}
		
		return requests.post(self.get_api_url() , params={"access_token":self.get_access_token()} , json=request_body).json()

	def __send_local_attachment(self , asset_type , file_location , recipient_id):
		request_body = MultipartEncoder(fields={
					"recipient":str({"id":recipient_id}),
					"message":str({"attachment":{"type":asset_type, "payload":{"is_reusable":"true"}}}),
					"filedata" : (os.path.basename(file_location) , open(file_location , "rb") , magic.Magic(mime=True).from_file(file_location))
					
		})
		headers = {"content-type":request_body.content_type}
		
		return requests.post(self.get_api_url() , params={"access_token":self.get_access_token()} , data=request_body , headers=headers).json()

	def send_local_image(self , image_location , recipient_id):
		return self.__send_local_attachment("image" , image_location , recipient_id)

	def send_local_video(self , video_location , recipient_id):
		return self.__send_local_attachment("video" , video_location , recipient_id)

	def send_local_audio(self , audio_location , recipient_id):
		return self.__send_local_attachment("audio" , audio_location , recipient_id)

	def send_local_file(self , file_location , recipient_id):
		return self.__send_local_attachment("file" , file_location , recipient_id)