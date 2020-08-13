import React, { Component } from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Container from 'react-bootstrap/Container';
import Table from 'react-bootstrap/Table';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import SearchBar from './components/SearchBar';


class App extends Component {
  state = {
      stockName: 'Enter a valid stock name to find opportunities!',
      body: []
  }

  setBody = (stockName) => {
      this.setState({
          stockName: stockName
      });
      if(stockName !== '') {
          this.setState({
              stockName: 'Getting data for ' + stockName + '...'
          });
          axios.get('http://127.0.0.1:5000/stock/' + stockName)
              .then((data) => {
                  this.setState({
                      stockName: stockName,
                      body: Object.keys(data['data'][stockName]).map((key) => 
                        <tr>
                            <td>{key}</td>
                            <td>{data['data'][stockName][key]}</td>
                        </tr>
                      )
                  });
              });
      }
  }

  render() {
      return (
          <Container>
              <Jumbotron >
                <h2 className='mb-4'>Conversion/Reversal Detector</h2>
                <Container>
                    <SearchBar setBody={this.setBody}/>
                </Container>
                <Container>
                    <h4 className='mt-3'> {this.state.stockName}</h4>
                    <Table bordered hover className='mt-3' size='sm'>
                        <thead>
                            <tr>
                                <th>Expiry Date</th>
                                <th>Price Diff</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.state.body}
                        </tbody>
                    </Table>
                </Container>
              </Jumbotron>
          </Container>
      );
  }
}

export default App;
