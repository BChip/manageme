from flask_restful import Resource, reqparse
from resources.__init__ import dbengine, managemeutil
import werkzeug

###########################################################################
read_user_post_parser = reqparse.RequestParser(bundle_errors=True)

read_user_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_user_post_parser.add_argument(
    'userID', dest='userID',
    location='json', required=False,
    type=managemeutil.verify_userIDNotExist,
    help='The user\'s ID. {error_msg}',
)

class readUser(Resource):
	def post(self):
		args = read_user_post_parser.parse_args()
		if args.userID is not None:
			return dbengine.readUserByID(args)
		else:
			return dbengine.readUsers(args)

###########################################################################

create_requirement_post_parser = reqparse.RequestParser(bundle_errors=True)

create_requirement_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

create_requirement_post_parser.add_argument(
    'estimate', dest='estimate',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s estimate. {error_msg}',
)

create_requirement_post_parser.add_argument(
    'desc', dest='desc',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s description. {error_msg}',
)

create_requirement_post_parser.add_argument(
    'name', dest='name',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s name. {error_msg}',
)

create_requirement_post_parser.add_argument(
    'softcap', dest='softcap',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s softcap. {error_msg}',
)
create_requirement_post_parser.add_argument(
    'hardcap', dest='hardcap',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s hardcap. {error_msg}',
)
create_requirement_post_parser.add_argument(
    'priority', dest='priority',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s priority. {error_msg}',
)

class createReq(Resource):
	def post(self):
		args = create_requirement_post_parser.parse_args()
		return dbengine.createReq(args)
	
###########################################################################

read_req_post_parser = reqparse.RequestParser(bundle_errors=True)

read_req_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_req_post_parser.add_argument(
    'reqID', dest='reqID',
    location='json', required=False,
    type=managemeutil.verify_valid_req_id,
    help='The req\'s ID. {error_msg}',
)

class readReq(Resource):
	def post(self):
		args = read_req_post_parser.parse_args()
		if args.reqID is not None:
			return dbengine.readReqByID(args)
		else:
			return dbengine.readReqs(args)
	

###########################################################################

read_team_post_parser = reqparse.RequestParser(bundle_errors=True)

read_team_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_team_post_parser.add_argument(
    'teamID', dest='teamID',
    location='json', required=False,
    type=managemeutil.verify_valid_team_id,
    help='The req\'s ID. {error_msg}',
)

class readTeam(Resource):
	def post(self):
		args = read_team_post_parser.parse_args()
		if args.teamID is not None:
			return dbengine.readTeamByID(args)
		else:
			return dbengine.readTeams(args)
	
###########################################################################

create_estimate_post_parser = reqparse.RequestParser(bundle_errors=True)

create_estimate_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

create_estimate_post_parser.add_argument(
    'reqID', dest='reqID',
    location='json', required=True,
    type=managemeutil.verify_valid_req_id,
    help='The req\'s ID. {error_msg}',
)

create_estimate_post_parser.add_argument(
    'estimateAmt', dest='estimateAmt',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The estimate\'s amount. {error_msg}',
)

class createEstimate(Resource):
	def post(self):
		args = create_estimate_post_parser.parse_args()
		return dbengine.createEstimate(args)
	
###########################################################################

#######################################################
read_permissions_parser = reqparse.RequestParser(bundle_errors=True)

read_permissions_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_permissions_parser.add_argument(
    'user_id', dest='user_id',
    location='json', required=False,
    type=managemeutil.verify_userIDNotExist,
    help='The user\'s ID. {error_msg}',
)

class readPermissions(Resource):
	def post(self):
		args = read_permissions_parser.parse_args()
		return dbengine.readPermissions(args)

#######################################################################


###########################################################################

create_team_member_parser = reqparse.RequestParser(bundle_errors=True)

create_team_member_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

create_team_member_parser.add_argument(
    'teamID', dest='teamID',
    location='json', required=True,
    type=managemeutil.verify_valid_team_id,
    help='The team\'s ID. {error_msg}',
)

create_team_member_parser.add_argument(
    'user_id', dest='user_id',
    location='json', required=True,
    type=managemeutil.verify_userIDNotExist,
    help='The user\'s ID. {error_msg}',
)

class createTeamMember(Resource):
	def post(self):
		args = create_team_member_parser.parse_args()
		return dbengine.createTeamMember(args)
	
###########################################################################



###########################################################################

read_team_members_parser = reqparse.RequestParser(bundle_errors=True)

read_team_members_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_team_members_parser.add_argument(
    'teamID', dest='teamID',
    location='json', required=True,
    type=managemeutil.verify_valid_team_id,
    help='The team\'s ID. {error_msg}',
)

class readTeamMembers(Resource):
	def post(self):
		args = read_team_members_parser.parse_args()
		return dbengine.readTeamMembers(args)
	
###########################################################################

'''
check valid file type : verify_valid_file_type
list file types
'''
###########################################################################

create_document_parser = reqparse.RequestParser(bundle_errors=True)

create_document_parser.add_argument(
    'token', dest='token',
    location='form', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

create_document_parser.add_argument(
    'fileTypeId', dest='fileTypeId',
    location='form', required=True,
    type=managemeutil.verify_valid_file_type,
    help='The document\'s file type id. {error_msg}',
)

create_document_parser.add_argument(
    'name', dest='name',
    location='form', required=True,
    help='The document\'s name. {error_msg}',
)

create_document_parser.add_argument(
    'desc', dest='desc',
    location='form', required=True,
    help='The doc\'s desc. {error_msg}',
)

create_document_parser.add_argument(
    'blob', dest='blob',
    location='files', required=True,
    type=werkzeug.datastructures.FileStorage,
    help='The doc\'s blob. {error_msg}',
)

class createDocument(Resource):
	def post(self):
		args = create_document_parser.parse_args()
		return dbengine.createDocument(args)
	
###########################################################################

###########################################################################

read_document_parser = reqparse.RequestParser(bundle_errors=True)

read_document_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_document_parser.add_argument(
    'doc_id', dest='doc_id',
    location='json', required=True,
    help='The document\'s file type id. {error_msg}',
)


class readDocument(Resource):
	def post(self):
		args = read_document_parser.parse_args()
		return dbengine.readDocument(args)
	
###########################################################################

###########################################################################

create_project_document_parser = reqparse.RequestParser(bundle_errors=True)

create_project_document_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

create_project_document_parser.add_argument(
    'project_uid', dest='project_uid',
    location='json', required=True,
    type=managemeutil.verify_valid_project_id,
    help='The file\'s project id. {error_msg}',
)

create_project_document_parser.add_argument(
    'doc_uid', dest='doc_uid',
    location='json', required=True,
    help='The document\'s doc_uid. {error_msg}',
)


class createProjectDocument(Resource):
	def post(self):
		args = create_project_document_parser.parse_args()
		return dbengine.createProjectDocument(args)
	
###########################################################################

###########################################################################

read_project_document_parser = reqparse.RequestParser(bundle_errors=True)

read_project_document_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_project_document_parser.add_argument(
    'project_uid', dest='project_uid',
    location='json', required=True,
    type=managemeutil.verify_valid_project_id,
    help='The file\'s project id. {error_msg}',
)

class readProjectDocument(Resource):
	def post(self):
		args = read_project_document_parser.parse_args()
		return dbengine.readProjectDocument(args)
	
###########################################################################

###########################################################################

read_document_filetypes_parser = reqparse.RequestParser(bundle_errors=True)

read_document_filetypes_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

class readDocumentFileTypes(Resource):
	def post(self):
		args = read_document_filetypes_parser.parse_args()
		return dbengine.readDocumentFileTypes(args)
	
###########################################################################

###########################################################################

read_req_by_projID_filetypes_parser = reqparse.RequestParser(bundle_errors=True)

read_req_by_projID_filetypes_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

read_req_by_projID_filetypes_parser.add_argument(
    'project_uid', dest='project_uid',
    location='json', required=True,
    type=managemeutil.verify_valid_project_id,
    help='The req\'s project id. {error_msg}',
)

class readReqByProjID(Resource):
	def post(self):
		args = read_req_by_projID_filetypes_parser.parse_args()
		return dbengine.readReqByProjID(args)
	
###########################################################################

###########################################################################

create_requirement_change_request_post_parser = reqparse.RequestParser(bundle_errors=True)

create_requirement_change_request_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

create_requirement_change_request_post_parser.add_argument(
    'estimate', dest='estimate',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s estimate. {error_msg}',
)

create_requirement_change_request_post_parser.add_argument(
    'desc', dest='desc',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s description. {error_msg}',
)

create_requirement_change_request_post_parser.add_argument(
    'name', dest='name',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s name. {error_msg}',
)

create_requirement_change_request_post_parser.add_argument(
    'softcap', dest='softcap',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s softcap. {error_msg}',
)
create_requirement_change_request_post_parser.add_argument(
    'hardcap', dest='hardcap',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s hardcap. {error_msg}',
)
create_requirement_change_request_post_parser.add_argument(
    'priority', dest='priority',
    location='json', required=True,
    #type=managemeutil.verify_projectNotExist,
    help='The req\'s priority. {error_msg}',
)

class createReqChangeRequest(Resource):
	def post(self):
		args = create_requirement_change_request_post_parser.parse_args()
		return dbengine.createReqChangeRequest(args)
	
###########################################################################

###########################################################################

accept_req_change_request_post_parser = reqparse.RequestParser(bundle_errors=True)

accept_req_change_request_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

accept_req_change_request_post_parser.add_argument(
    'reqID', dest='reqID',
    location='json', required=True,
    type=managemeutil.verify_valid_req_id,
    help='The req\'s ID. {error_msg}',
)

class acceptReqChangeRequest(Resource):
	def post(self):
		args = accept_req_change_request_post_parser.parse_args()
		return dbengine.acceptReqChangeRequest(args)

###########################################################################


###########################################################################

reject_req_change_request_post_parser = reqparse.RequestParser(bundle_errors=True)

reject_req_change_request_post_parser.add_argument(
    'token', dest='token',
    location='json', required=True,
    type=managemeutil.verify_request_token,
    help='The user\'s token {error_msg}',
)

reject_req_change_request_post_parser.add_argument(
    'reqID', dest='reqID',
    location='json', required=True,
    type=managemeutil.verify_valid_req_id,
    help='The req\'s ID. {error_msg}',
)

class rejectReqChangeRequest(Resource):
	def post(self):
		args = reject_req_change_request_post_parser.parse_args()
		return dbengine.rejectReqChangeRequest(args)

###########################################################################