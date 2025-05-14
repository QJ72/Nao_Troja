def look_for_services(session, name_of_service = "AL"):
    services = session.services()
    for service in services:
        if name_of_service in service["name"] :
            print(service["name"])