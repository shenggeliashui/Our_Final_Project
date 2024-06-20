<template>
  <div class="calendar">
    <div class="header">
      <button @click="prevMonth">&lt;</button>
      <h2>{{ monthNames[currentMonth] }} {{ currentYear }}</h2>
      <button @click="nextMonth">&gt;</button>
    </div>
    <div class="weekdays">
      <div v-for="(day, index) in weekdays" :key="index">{{ day }}</div>
    </div>
    <div class="days">
      <div
        v-for="(day, index) in days"
        :key="index"
        :class="{ today: isToday(day), empty: !day }"
      >
        {{ day }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Calendar',
  data () {
    return {
      currentDate: new Date(),
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      monthNames: [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
      ],
      weekdays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    }
  },
  computed: {
    days () {
      const daysArray = []
      const daysInCurrentMonth = this.daysInMonth(this.currentMonth, this.currentYear)
      const firstDay = this.firstDayOfMonth(this.currentMonth, this.currentYear)

      for (let i = 0; i < firstDay; i++) {
        daysArray.push(null)
      }

      for (let i = 1; i <= daysInCurrentMonth; i++) {
        daysArray.push(i)
      }

      return daysArray
    }
  },
  methods: {
    daysInMonth (month, year) {
      return new Date(year, month + 1, 0).getDate()
    },
    firstDayOfMonth (month, year) {
      return new Date(year, month, 1).getDay()
    },
    prevMonth () {
      if (this.currentMonth === 0) {
        this.currentMonth = 11
        this.currentYear--
      } else {
        this.currentMonth--
      }
    },
    nextMonth () {
      if (this.currentMonth === 11) {
        this.currentMonth = 0
        this.currentYear++
      } else {
        this.currentMonth++
      }
    },
    isToday (day) {
      if (day === null) return false
      const today = new Date()
      return (
        day === today.getDate() &&
        this.currentMonth === today.getMonth() &&
        this.currentYear === today.getFullYear()
      )
    }
  }
}
</script>

<style scoped>
.calendar {
    width: 300px;
    border: 1px solid #ccc;
    border-radius: 5px;
    overflow: hidden;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #f0f0f0;
    padding: 10px;
}

.weekdays, .days {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    text-align: center;
}

.weekdays div {
    background-color: #ddd;
    padding: 10px 0;
}

.days div {
    padding: 10px 0;
    cursor: pointer;
}

.days div.empty {
    background-color: #f9f9f9;
}

.days div.today {
    background-color: #87ceeb;
    color: #fff;
}
</style>
