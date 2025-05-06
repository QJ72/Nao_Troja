import qi
from PIL import Image
from request_openai import send_image_to_server

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    application = qi.Application(url="tcp://192.168.1.101:9559")
    application.start()
    print("Application started.")

    posture = application.session.service("ALRobotPosture")
    photo_capture = application.session.service("ALPhotoCapture")
    video_service = application.session.service("ALVideoDevice")

    """"
    print(posture.getPosture())
    if posture.getPosture() != "Stand":
        posture.goToPosture("Stand", 0.4) #second parameter is speed

    else :
        posture.goToPosture("Crouch", 0.4)
    """

    resolution = 2  # VGA
    colorSpace = 11  # RGB

    videoClient = video_service.subscribe("python_client", resolution, colorSpace, 5)

    naoImage = video_service.getImageRemote(videoClient)

    video_service.unsubscribe(videoClient)

    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
    image_string = str(bytearray(array))

    im = Image.frombytes("RGB", (imageWidth, imageHeight), image_string)

    im.save("camImage.png", "PNG")

    send_image_to_server("./camImage.png")

    application.stop()