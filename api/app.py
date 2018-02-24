'''
Dependencies:
	install python 2.7.14
	install latest pip
	pip install flask
	pip install flask-restful
	pip install mysqlclient
	pip install validate_email
	pip install Flask-HTTPAuth
	pip install -U flask-cors
	pip install Flask-WTF
	pip install simplejson
	pip install Werkzeug
'''
# import dependencies
from sys import argv
import sys
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# routing classes
from resources.index import index
from resources.helloworld import helloworld
from resources.user import user
from resources.login import login
from resources.register import register
from resources.createproject import createproject
from resources.getprojects import getprojects
from resources.createteam import createteam
from resources.viewhours import viewhours
from resources.viewprojecthours import viewprojecthours
from resources.clockin import clockin
from resources.clockout import clockout
from resources.disableuser import disableuser
from resources.assignprivilage import assignprivilage
from resources.revoke_privilage import revoke_privilage
from resources.read_estimate_by_project_id import read_estimate_by_project_id
from resources.read_estimate_by_req_id import read_estimate_by_req_id
from resources.read_timecaps_by_project_id import read_timecaps_by_project_id
from resources.create_read import readUser, createReq, readReq, readTeam, createEstimate, readPermissions, createTeamMember, readTeamMembers, createDocument, readDocument, createProjectDocument, readProjectDocument, readDocumentFileTypes, readReqByProjID 
from resources.update_delete import updateProject, deleteProject, updateTeamLead, deleteTeamMember, deleteProjectDocument

# define the app and run it
app = Flask(__name__)
api = Api(app)
CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}})

# @app.after_request
# def after_request(response):
  # response.headers.add('Access-Control-Allow-Origin', '*')
  # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  # return response

# routing paths
api.add_resource(index, '/')
api.add_resource(helloworld, '/helloworld', '/helloworld/')
api.add_resource(user, '/user', '/user/')
api.add_resource(login, '/user/login', '/user/login/')
api.add_resource(register, '/user/create', '/user/create/')
api.add_resource(createproject, '/project/create', '/project/create/')
api.add_resource(getprojects, '/project/get', '/project/get/')
api.add_resource(createteam, '/team/create', '/team/create/')
api.add_resource(viewhours, '/clock/get', '/clock/get/')
api.add_resource(viewprojecthours, '/project/hours/get', '/project/hours/get/')
api.add_resource(clockin, '/clock/in', '/clock/in/')
api.add_resource(clockout, '/clock/out', '/clock/out/')
api.add_resource(disableuser, '/user/disable', '/user/disable/')
api.add_resource(assignprivilage, '/privilage/assign', '/privilage/assign/')
api.add_resource(revoke_privilage, '/privilage/revoke', '/privilage/revoke/')
api.add_resource(read_estimate_by_project_id, '/project/estimate/get', '/project/estimate/get/')
api.add_resource(read_estimate_by_req_id, '/requirement/estimate/get', '/requirement/estimate/get/')
api.add_resource(read_timecaps_by_project_id, '/project/timecaps/get', '/project/timecaps/get/')
### capstone2
api.add_resource(readUser, '/user/get', '/user/get/')
api.add_resource(createReq, '/requirement/create', '/requirement/create/')
api.add_resource(readReq, '/requirement/get', '/requirement/get/')
api.add_resource(readTeam, '/team/get', '/team/get/')
api.add_resource(createEstimate, '/requirement/estimate/create', '/requirement/estimate/create/')
### capstone 3
api.add_resource(updateProject, '/project/update', '/project/update/')
api.add_resource(deleteProject, '/project/delete', '/project/delete/')

#### 4
api.add_resource(readPermissions, '/privilage/get', '/privilage/get/')
api.add_resource(createTeamMember, '/team/member/create', '/team/member/create/')
api.add_resource(updateTeamLead, '/team/member/lead', '/team/member/lead/')
api.add_resource(readTeamMembers, '/team/member/get', '/team/member/get/')
api.add_resource(deleteTeamMember, '/team/member/delete', '/team/member/delete/')
api.add_resource(createDocument, '/document/create', '/document/create/')
api.add_resource(readDocument, '/document/get', '/document/get/')
api.add_resource(createProjectDocument, '/project/document/create', '/project/document/create/')
api.add_resource(readProjectDocument, '/project/document/get', '/project/document/get/')
api.add_resource(deleteProjectDocument, '/project/document/delete', '/project/document/delete/')
api.add_resource(readDocumentFileTypes, '/document/type/get', '/document/type/get/')
api.add_resource(readReqByProjID, '/project/req/get', '/project/req/get/')

# for debugging, running indivisually with -debug param
if '-debug' in argv:
	app.run(debug=True)
