TO DO:

1) "Converse"  - domination-TAG parser for Linux process tree
2) "Druid" - PMCFG-Metagrammar two-level metagrammar parser for abstract Tree Notation

extended pstree output example:

Format:(name p g s)
|- systemd 1 1 1
  | |- systemd-journald 244 244 244
...
  | |- lightdm 856 856 856
  | | |- Xorg 1073 1073 1073
  | | `_ lightdm 1316 856 856
  | |   `_ upstart 1344 1344 1344
  | |     |- unity-settings-daemon 1610 1610 1610
  | |     | `_ syndaemon 1825 1610 1610
  | |     |- gnome-session-binary 1619 1619 1619
  | |     | |- nm-applet 1758 1619 1619
  | |     | |- update-notifier 2146 1619 1619
  | |     | `_ deja-dup-monitor 2172 1619 1619
  | |     |- gconfd-2 4034 1444 1444›
  | |     `_ firefox 4345 1802 1802
  | |       |- Web Content 4480 1802 1802
  | |       `_ Web Content 4508 1802 1802
...
  `_ kthreadd 2 0 0
    |- kworker/0:0H 4 0 0
    |- mm_percpu_wq 6 0 0
    |- ksoftirqd/0 7 0 0
    |- rcu_sched 8 0 0
    |- rcu_bh 9 0 0
