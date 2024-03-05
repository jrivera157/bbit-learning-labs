# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys
import time

from solution.consumer_sol import mqConsumer  # pylint: disable=import-error

def main(sector: str, queueName: str) -> None:
    
    # Implement Logic to Create Binding Key from the ticker and sector variable -  Step 2
    bindingKey = f'{sector}.#'
    
    consumer = mqConsumer(binding_key=bindingKey,exchange_name="Tech Lab Topic Exchange",queue_name=queueName)    
    consumer.startConsuming()    


if __name__ == "__main__":

    # Implement Logic to read the sector and queueName string from the command line and save them - Step 1
    if len(sys.argv) != 3:
        print(f'Error, wrong number of arguments. Needs args in the format of: consume.py <sector> <queueName>. Only got {len(sys.argv)} args')
        sys.exit(-3)

    sector = sys.argv[1]

    # i could pass queue name here although i feel lazy so to make sure i never mess up, i could just pass in a timestamp so it's always unique 
    # queue = sys.argv[2]

    fake_name = f'{time.time()}'
    print(f'faking the queue name with seconds from epoch: {fake_name}')
    queue = fake_name
   
    sys.exit(main(sector,queue))
