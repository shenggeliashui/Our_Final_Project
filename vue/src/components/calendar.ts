// calendar.ts

import { ref, computed } from 'vue'

export const useCalendar = () => {
  const currentDate = ref(new Date())
  const currentMonth = ref(currentDate.value.getMonth())
  const currentYear = ref(currentDate.value.getFullYear())

  const monthNames = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ]
  const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

  const daysInMonth = (month: number, year: number) => {
    return new Date(year, month + 1, 0).getDate()
  }

  const firstDayOfMonth = (month: number, year: number) => {
    return new Date(year, month, 1).getDay()
  }

  const days = computed(() => {
    const daysArray: (number | null)[] = []
    const daysInCurrentMonth = daysInMonth(currentMonth.value, currentYear.value)
    const firstDay = firstDayOfMonth(currentMonth.value, currentYear.value)

    for (let i = 0; i < firstDay; i++) {
      daysArray.push(null)
    }

    for (let i = 1; i <= daysInCurrentMonth; i++) {
      daysArray.push(i)
    }

    return daysArray
  })

  const prevMonth = () => {
    if (currentMonth.value === 0) {
      currentMonth.value = 11
      currentYear.value--
    } else {
      currentMonth.value--
    }
  }

  const nextMonth = () => {
    if (currentMonth.value === 11) {
      currentMonth.value = 0
      currentYear.value++
    } else {
      currentMonth.value++
    }
  }

  const isToday = (day: number | null): boolean => {
    if (day == null) return false
    const today = new Date()
    return (
      day === today.getDate() &&
      currentMonth.value === today.getMonth() &&
      currentYear.value === today.getFullYear()
    )
  }

  return {
    currentMonth,
    currentYear,
    monthNames,
    weekdays,
    days,
    prevMonth,
    nextMonth,
    isToday
  }
}
