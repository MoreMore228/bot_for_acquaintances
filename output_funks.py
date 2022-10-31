def conclusion_of_the_questionnaire(data={'int_user': 1, 'user_id': 984453688, 'user_name': '@mishanya', 'img_path': 'jhwdf8372', 'name': 'МИША', 'user_age': 10, 'user_city': 'Азербайджан', 'user_info': 'я аресивная ', 'user_flag': 0}):
    return data["img_path"], "{0}, {1}, {2} \n {3}".format(
        data["name"], 
        data["user_age"],
        data["user_city"],
        data["user_info"]
        )


