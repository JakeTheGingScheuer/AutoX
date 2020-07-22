import React from "react";
import CarListByMake from "./components/carListByMake";


class App extends React.Component {

    render() {
        return (
            <div className="app">
                <CarListByMake />
            </div>
        );
    }
}

export default App;