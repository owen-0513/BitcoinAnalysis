import { createRouter, createWebHistory } from 'vue-router';
import BitcoinData from './components/BitcoinData.vue';
import SelfIntroduction from './components/about.vue';
import Home from './components/Home.vue';
import ProjectPortfolio from './components/ProjectPortfolio.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/bitcoin',
        name: 'BitcoinData',
        component: BitcoinData,
    },
    {
        path: '/about',
        name: 'SelfIntroduction',
        component: SelfIntroduction,
    },
    {
        path: '/portfolio',
        name: 'ProjectPortfolio',
        component: ProjectPortfolio
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
