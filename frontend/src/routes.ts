// pages
import Donate from "./pages/Donate";
import Distribute from "./pages/Distribute";
import Report from "./pages/Report";

// other
import {FC} from "react";

// interface
interface Route {
    key: string,
    title: string,
    path: string,
    enabled: boolean,
    component: FC<{}>
}

export const routes: Array<Route> = [
    {
        key: 'donate-route',
        title: 'Donate',
        path: '/Donate',
        enabled: true,
        component: Donate
    },
    {
        key: 'distribute-route',
        title: 'Distribute',
        path: '/distribute',
        enabled: true,
        component: Distribute
    },
    {
        key: 'report-route',
        title: 'Report',
        path: '/report',
        enabled: true,
        component: Report
    }
]