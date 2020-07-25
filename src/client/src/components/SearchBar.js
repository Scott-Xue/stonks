import { Component } from 'react';
import PropTypes from 'prop-types';

export default class SearchBar extends Component {

    state = {
        stockName: ''
    }

    searchFor = () => {
        this.props.findOpportunities(this.state.stockName);
        this.setState({stockName: ''});
    }

    updateStock = (e) => this.setState({[e.target.name]: e.target.value})
    
    render() {
        return (
            <div>
                <button type="button" onClick={this.searchFor}>Search</button>
                <input 
                    type="text" 
                    name="stockName"
                    value = {this.state.stockName}
                    onChange = {this.updateStock}
                ></input>
            </div>
        );
    }
}

SearchBar.propTypes = {
    findOpportunities: PropTypes.func.isRequired
};