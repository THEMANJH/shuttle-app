// 시간표 데이터
const schedule = [
    { id: 1, time: "09:00 AM" },
    { id: 2, time: "12:00 PM" },
    { id: 3, time: "03:00 PM" }
  ];
  
  // 예약 데이터 저장소
  const reservations = [];
  
  // HTML 요소 가져오기
  const scheduleList = document.getElementById("schedule-list");
  const reservationsList = document.getElementById("reservations-list");
  const reserveBtn = document.getElementById("reserve-btn");
  const nameInput = document.getElementById("name");
  
  // 시간표 출력
  schedule.forEach((shuttle) => {
    const li = document.createElement("li");
    li.textContent = shuttle.time;
    scheduleList.appendChild(li);
  });
  // 안녕하세요
// 안녕하세요2
  //안녕하세요3
  //최장혁 바보ㅇㅇ

  // 예약 버튼 클릭 이벤트
  reserveBtn.addEventListener("click", () => {
    const name = nameInput.value;
    if (name) {
      reservations.push({ name, time: schedule[0].time }); // 기본으로 첫 번째 시간 선택
      updateReservations();
      nameInput.value = ""; // 입력창 초기화
      alert("예약이 완료되었습니다!");
    } else {
      alert("이름을 입력하세요!");
    }
  });
  // 밥 뭐 먹을래
  // 예약 목록 업데이트
  function updateReservations() {
    reservationsList.innerHTML = ""; // 기존 목록 지우기
    reservations.forEach((reservation) => {
      const li = document.createElement("li");
      li.textContent = `${reservation.name} - ${reservation.time}`;
      reservationsList.appendChild(li);
    });
  }
  