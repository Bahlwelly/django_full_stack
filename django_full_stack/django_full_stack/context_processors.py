def role (request) :
    if request.user.is_authenticated :
        return { "role" : request.user.role }

    return {"role" : None}