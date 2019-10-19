# usage
```bash
# possible keys
data_session_associated
data_session_avg_reward
data_session_deauthed
data_session_epochs
data_session_handshakes
data_session_max_reward
data_session_min_reward
data_session_peers
data_session_train_epochs

# top units sorted by captured networks
./rank.py --max 10 --key networks

# top units sorted by epochs
./rank.py --max 10 --key data_session_epochs

# top units sorted by deauths
./rank.py --max 10 --key data_sessions_deauthed
```

## example
`./rank.py --max 10 --key networks`

![Example](images/example.png)
