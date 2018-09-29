import network
from auklet.monitoring import Monitoring

def main():
	wlan = network.WLAN(mode=network.WLAN.STA)
	print(wlan.ifconfig())

	auklet_monitoring = Monitoring


if __name__ == "__main__":
	main()