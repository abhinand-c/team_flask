from flask import render_template, redirect, request

from . import app
from database import operations as db_op

def get_obj(dict_list, key, value):
    for i in dict_list:
        if(i[key]==value):
            return i
    return None

def clean_dict(obj):
    data = {}
    for key, value in obj.items():
        if value:
            data[key]=value
    return data

def get_or_none(obj, key):
    if obj:
        return obj[key]
    return None

@app.route('/')
def home():
    user_list=db_op.get_data("USER")
    team_list = db_op.get_data("TEAM")
    member_list=db_op.get_data("MEMBERSHIP")

    for team in team_list:
        team["manager"] = get_or_none(get_obj(user_list, "id" ,team["manager"]),"name")

    for member in member_list:
        member["user"] = get_or_none(get_obj(user_list, "id", member["user"]),"name")
        member["team"] = get_or_none(get_obj(team_list, "id" ,member["team"]),"name")

    return render_template(
        'list.html',
        title="Dash",
        user_list=user_list,
        team_list=team_list,
        member_list=member_list,
    )

@app.route('/user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        db_op.add_data('USER', clean_dict(request.form.to_dict()))
        return redirect("/")

    return render_template(
        'user.html',
        title="Add User",
    )


@app.route('/team', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        db_op.add_data('TEAM',clean_dict(request.form.to_dict()))
        return redirect("/")

    user_list=db_op.get_data("USER")

    return render_template(
        'team.html',
        title="Add Team",
        user_list=user_list,
    )


@app.route('/member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        db_op.add_data('MEMBERSHIP',clean_dict(request.form.to_dict()))
        return redirect("/")

    user_list=db_op.get_data("USER")
    team_list = db_op.get_data("TEAM")

    return render_template(
        'member.html',
        title="Add Membership",
        user_list=user_list,
        team_list=team_list,
    )
