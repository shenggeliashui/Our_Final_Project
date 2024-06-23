import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage'
import WriteFromMemory from '@/components/WriteFromMemory/WriteFromMemory'
import MemoryTenWords from '@/components/MemoryWords/MemoryTenWords'
import FinishTenWords from '@/components/MemoryWords/FinishTenWords'
const routes=[
    {
        path:'/write-from-memory',
        name:'WriteFromMemory',
        component:WriteFromMemory
    },
    {
        path:'/',
        name:"HomePage",
        component:HomePage
    },
    {
        path:'/memory-ten-words',
        name:'MemoryTenWords',
        component:MemoryTenWords
    },
    {
        path:'/memory-ten-words/finish-ten-words',
        name:'FinishTenWords',
        component:FinishTenWords
    }
]
const router=createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router