from numpy.random import default_rng
rng = default_rng()

u1 = 6
u2 = 4
replications = 10000

times_a_ocurred = 0
times_b_ocurred = 0
total_wait = 0

for x in range(replications):
  service_1_time = rng.exponential(1/u1)
  service_2_time = [None] * 3

  service_2_arrival_time = [None] * 3
  service_2_start_time = [None] * 3
  service_2_finish_time = [None] * 3

  service_2_arrival_time[0] = 0
  service_2_start_time[0] = 0

  for i in range(3):
    service_2_time[i] = rng.exponential(1/u2)

  service_2_finish_time[0] = service_2_time[0]

  service_2_arrival_time[1] = service_2_arrival_time[0]
  service_2_start_time[1] = max(service_2_arrival_time[1], service_2_finish_time[0])
  service_2_finish_time[1] = service_2_start_time[1] + service_2_time[1]

  service_2_arrival_time[2] = service_2_arrival_time[1] + service_1_time
  service_2_start_time[2] = max(service_2_arrival_time[2], service_2_finish_time[1])
  service_2_finish_time[2] = service_2_start_time[2] + service_2_time[2]

  if service_2_arrival_time[2] < service_2_finish_time[0]:
    times_a_ocurred += 1
  
  if service_2_arrival_time[2] < service_2_finish_time[1]:
    times_b_ocurred += 1

  total_wait += service_2_finish_time[2]

print('(a)', '\nanalitical', u1/(u1+u2), '\nsimulation', times_a_ocurred/replications)
print('(b)', '\nanalitical', u1/(u1+u2)+((u2/(u1+u2))*(u1/(u1+u2))), '\nsimulation', times_b_ocurred/replications)
print('(c)', '\nanalitical', (1/u1)+(1/u2)+(u1/(u2*(u1+u2)))+(1/u2*((u1/(u1+u2))+((u2/(u1+u2))*(u1/(u1+u2))))), '\nsimulation', total_wait/replications)
  