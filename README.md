# Ethereum ETL

###  ETL

1. 自定义csv格式  

   blocks.csv

   | Column            | Type       |
   | ----------------- | ---------- |
   | number            | bigint     |
   | hash              | hex_string |
   | parent_hash       | hex_string |
   | nonce             | hex_string |
   | sha3_uncles       | hex_string |
   | logs_bloom        | hex_string |
   | transactions_root | hex_string |
   | state_root        | hex_string |
   | receipts_root     | hex_string |
   | miner             | address    |
   | difficulty        | numeric    |
   | total_difficulty  | numeric    |
   | size              | bigint     |
   | extra_data        | hex_string |
   | gas_limit         | bigint     |
   | gas_used          | bigint     |
   | timestamp         | bigint     |
   | transaction_count | bigint     |
   | base_fee_per_gas  | bigint     |
   | transaction1      |            |
   | transaction2      |            |
   | ...               |            |

2. 实时更新

   1. 监控 
   2. 导出 将新生成的区块  做1中的合并操作 追加到blocks.csv文件中

## demo

查询实例 各两个 

1. 静态（getBlockByTimestamp）
2. 动态（swap）
