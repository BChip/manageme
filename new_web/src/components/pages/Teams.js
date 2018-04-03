import React, { Component } from 'react';
import {
  Row,
  Col,
  Card,
  CardBody,
  Button,
} from 'reactstrap';
import { withRouter } from 'react-router-dom';
import { getLocalToken } from '../../utils/Auth';
import RecentProjects from '../dashboard/RecentProjects';
import RecentRequirements from '../dashboard/RecentRequirements';
import { getTeams } from '../../utils/HttpHelper';
import MyTeams from '../teams/MyTeams';

class Teams extends Component {
  constructor(props) {
    super(props);

    this.state = {
    };
  }

  render() {
    return (
      <div>
        <MyTeams />

      </div>
    );
  }
}

export default withRouter(Teams);