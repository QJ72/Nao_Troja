import qi

class NaoVisionManager:
    def __init__(self,session: qi.Session):
        self.video_service = session.service("ALVideoDevice")
        self.video_client = self.video_service.subscribe("video_client", 2, 11, 5)

    def get_video_service(self):
        return self.video_service

    def get_video_client(self):
        return self.video_client