export async function getToken(user, pass) {
  const res = await fetch('https://api.manageme.tech/user/login', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      username: user,
      password: pass,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getTime(tok) {
  const res = await fetch('https://api.manageme.tech/clock/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function clockIn(tok, reqID) {
  const res = await fetch('https://api.manageme.tech/clock/in', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      req_id: reqID,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function clockOut(tok, reqID) {
  const res = await fetch('https://api.manageme.tech/clock/out', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      req_id: reqID,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getEstimate(tok, projId) {
  const res = await fetch('https://api.manageme.tech/project/estimate/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      project_id: projId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getRequirementEstimates(tok, reqId) {
  const res = await fetch('https://api.manageme.tech/requirement/estimate/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      req_id: reqId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getTimeCaps(tok, projId) {
  const res = await fetch('https://api.manageme.tech/project/timecaps/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      project_id: projId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getProjects(tok) {
  const res = await fetch('https://api.manageme.tech/project/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getProjectHours(tok, projId) {
  const res = await fetch('https://api.manageme.tech/project/hours/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      uid: projId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getMyInfo(tok) {
  const res = await fetch('https://api.manageme.tech/util/custom', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      paramArr: [tok],
      spName: 'sp_getMyInfo',
    }),
  });
  const json = await res.json();
  return [json, res.status];
 }

export async function getUserInfoByUserId(tok, userId) {
  const res = await fetch('https://api.manageme.tech/user/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      userID: userId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getUserInfo(tok) {
  const res = await fetch('https://api.manageme.tech/user/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getRequirementById(tok, reqId) {
  const res = await fetch('https://api.manageme.tech/requirement/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      reqID: reqId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getRequirements(tok) {
  const res = await fetch('https://api.manageme.tech/requirement/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getTeamById(tok, teamId) {
  const res = await fetch('https://api.manageme.tech/team/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      teamID: teamId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getTeams(tok) {
  const res = await fetch('https://api.manageme.tech/team/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getRequirementsByProjectId(tok, projectId) {
  const res = await fetch('https://api.manageme.tech/project/req/get', {
    method: 'POST',
    headers:
        { 'content-type': 'application/json' },
    body: JSON.stringify({
      token: tok,
      project_uid: projectId,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}

export async function getAllPerms(token) {
  const res = await fetch('https://api.manageme.tech/privilage/get', {
    method: 'POST',
    headers:
            { 'content-type': 'application/json' },
    body: JSON.stringify({
      token,
    }),
  });
  const json = await res.json();
  return [json, res.status];
}
