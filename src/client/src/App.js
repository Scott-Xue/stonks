import React, { Component } from 'react';
import axios from 'axios';
import './App.css';
import SearchBar from './components/SearchBar';


class App extends Component {
  state = {
      stockName: '',
      body: ''
  }

  setBody = (stockName) => {
      this.setState({
          stockName: stockName
      });
      if(stockName !== '') {
          axios.get('http://127.0.0.1:5000/stock/' + stockName)
              .then((data) => {
                  this.setState({
                      body: data['data']
                  });
              });
      }
  }

  render() {
      return (
          <div className="App">
              <SearchBar setBody={this.setBody}/>
              <div class='container'>
                <h1> {this.state.stockName}</h1>
                <p>{this.state.body}</p>
              </div>
          </div>
      );
  }
}

export default App;
