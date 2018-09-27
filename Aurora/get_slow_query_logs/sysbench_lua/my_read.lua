#!/usr/bin/env sysbench
-- Copyright (C) 2006-2017 Alexey Kopytov <akopytov@gmail.com>

-- This program is free software; you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation; either version 2 of the License, or
-- (at your option) any later version.

-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.

-- You should have received a copy of the GNU General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

-- ----------------------------------------------------------------------
-- Read-Only OLTP benchmark
-- ----------------------------------------------------------------------

require("oltp_common")

function prepare_statements()
   prepare_point_selects()

   if not sysbench.opt.skip_trx then
      prepare_begin()
      prepare_commit()
   end

   if sysbench.opt.range_selects then
      prepare_simple_ranges()
      prepare_sum_ranges()
      prepare_order_ranges()
      prepare_distinct_ranges()
   end
end


function sendQuery(q)

    --print(q)
    --begin()
    con:query(q)
    --commit()
    
end

function event()

   --if not sysbench.opt.skip_trx then
   --   begin()
   --end

   --execute_point_selects()

   --if sysbench.opt.range_selects then
      --execute_simple_ranges()
      --execute_sum_ranges()
      --execute_order_ranges()
      --execute_distinct_ranges()
   --end
   --con:query('select * from information_schema.tables')
   --con:query('select sleep(1)')
   --con:query("SELECT \t/*+ [icms-api].com.lotte.icms.api.dao.IcmsUserReadOnlyDAO.selectUserInfoDetail */\n\t\t\t\t*\n\t\tFROM \tst_user\n\t\tWHERE \tcsco_id = 'ELLOTTE'\n\t\tAND \tsys_dvs_cd = '02'\n\t\tAND \tBINARY user_id = 'shlee01';")
   --con:query("INSERT INTO ltcmstdev.test_sysbench01(col2) values('test')")
   --con:query('select * from information_schema.columns')

   --if not sysbench.opt.skip_trx then
   --   commit()
   --end
   --
   --print("SELECT \t/*+ [icms-api].com.lotte.icms.api.dao.IcmsUserReadOnlyDAO.selectUserInfoDetail */\n\t\t\t\t*\n\t\tFROM \tst_user\n\t\tWHERE \tcsco_id = 'ELLOTTE'\n\t\tAND \tsys_dvs_cd = '02'\n\t\tAND \tBINARY user_id = 'shlee01';")

i=0
   for line in io.lines("slow_stuser.sql") do
       --print(line)
       --print(line)
       q=line:gsub([[\n]],"\n") 
       q=q:gsub([[\t]],"\t") 
       --os.execute("sleep " .. tonumber(1))
       if q~='' then 
          --print(q)
          --begin()
          --con:query(q)
          --commit()
          if pcall(sendQuery,q) then
              --print("Main Success")
              i=i+1
          else
              --print(q)
              print("Main Failure")
              print(q)
          end
       end

       
       --if i%100 == 0 then
       --    os.execute("sleep " .. tonumber(1))
       --end
       

   end
--os.execute("sleep " .. tonumber(1))
print(i)

end

