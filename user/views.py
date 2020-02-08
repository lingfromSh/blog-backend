from . import user


@user.route("/<uuid:id>")
def get_user(id):
    return f"< user:{id} > Hello, World!"


@user.route("/", methods=["POST"])
def get_users():
    return "asdsad"
