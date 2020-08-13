import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import FormControl from 'react-bootstrap/FormControl';
import InputGroup from 'react-bootstrap/InputGroup';
import PropTypes from 'prop-types';

export default class SearchBar extends Component {

    state = {
        stockName: ''
    }

    searchFor = () => {
        this.props.setBody(this.state.stockName);
        this.setState({stockName: ''});
    }

    updateStock = (e) => this.setState({[e.target.name]: e.target.value})
    
    render() {
        return (
            <div>
                <InputGroup>
                    <Button type="button" onClick={this.searchFor}>Search</Button>
                    <FormControl 
                        placeholder="Enter stock name"
                        type="text" 
                        name="stockName"
                        value = {this.state.stockName}
                        onChange = {this.updateStock}
                    ></FormControl>
                </InputGroup>
            </div>
        );
    }
}

SearchBar.propTypes = {
    setBody: PropTypes.func.isRequired
};