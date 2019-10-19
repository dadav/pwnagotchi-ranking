# usage
```bash
# possible keys
# ./rank.py --list
data_session_associated
data_session_avg_reward
data_session_deauthed
data_session_epochs
data_session_handshakes
data_session_max_reward
data_session_min_reward
data_session_peers
data_session_train_epochs
data_advertisement_epoch
data_advertisement_policy_advertise
data_advertisement_policy_ap_ttl
data_advertisement_policy_associate
data_advertisement_policy_bored_num_epochs
data_advertisement_policy_deauth
data_advertisement_policy_excited_num_epochs
data_advertisement_policy_hop_recon_time
data_advertisement_policy_max_inactive_scale
data_advertisement_policy_max_interactions
data_advertisement_policy_max_misses_for_recon
data_advertisement_policy_min_recon_time
data_advertisement_policy_min_rssi
data_advertisement_policy_recon_inactive_multiplier
data_advertisement_policy_recon_time
data_advertisement_policy_sad_num_epochs
data_advertisement_policy_sta_ttl
data_advertisement_pwnd_run
data_advertisement_pwnd_tot
data_advertisement_uptime
data_brain_born_at
data_brain_epochs_lived
data_brain_epochs_trained
data_brain_rewards_best
data_brain_rewards_worst
networks

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
