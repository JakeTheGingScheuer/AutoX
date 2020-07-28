import React from "react";
import "core-js/stable";
import "regenerator-runtime/runtime";
import CarList from "./carList";

export default class CarListByMake extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true,
            car_data: null
        }
    }

    async componentDidMount() {
        const url = 'http://localhost:5000/api/street_class/';
        const response = await fetch(url, {headers: {'Access-Control-Allow-Origin': '*'}});
        await response.json().then((result)=>{
            this.setState({car_data: result, loading: false})
        })
    }

    render() {
        if (this.state.loading) {
            return <div>Loading...</div>
        }

        if (!this.state.car_data) {
            return <div>No car data...</div>
        }
        return (
            <div>
                <CarList data={this.state.car_data}/>
            </div>
        );
    }
}