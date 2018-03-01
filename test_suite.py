from myBlockchain import *

class test_suite():
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.root = Tk()
        self.block_frame = Frame(self.root)
        self.input_frame = Frame(self.root, height=7, width=3)
        self.index_frame = Frame(self.root, height=7, width=3)
        self.blockchain_frame = Frame(self.root, height=7, width=3)
        self.block_frame.pack(side=LEFT)
        self.input_frame.pack(side=LEFT)
        self.index_frame.pack(side=LEFT)
        self.blockchain_frame.pack(side=TOP)

        self.block_label = Label(self.block_frame, text="Block Info:", fg="black")
        self.block_label.grid(sticky=E)

        self.input_label = Label(self.input_frame, text="Input data:", fg="black")
        self.input_label.grid(sticky=N)
        self.data_entry = Entry(self.input_frame)
        self.data_entry.grid(row=1,column=0, sticky=E)
        self.mine_data_button = Button(self.input_frame, text="Mine block", command=self.update_fields)
        self.mine_data_button2 = Button(self.input_frame, text="Mine 10 blocks", command=self.update_loop)
        self.mine_data_button3 = Button(self.input_frame, text="Mine X blocks", command=self.update_X)
        self.mine_data_button.grid(row=2, column=0)
        self.mine_data_button2.grid(row=3, column=0)
        self.mine_data_button3.grid(row=4, column=0)

        self.difficulty_label = Label(self.input_frame, text="Current difficulty: ", fg="black")
        self.difficulty_label.grid(row=5, column=0, sticky=W)
        self.difficulty_field = Label(self.input_frame, text=self.blockchain.getLatestBlock().getDifficulty())
        self.difficulty_field.grid(row=5, column=1, sticky=W)

        self.index_label = Label(self.index_frame, text="Index block:", fg="black")
        self.index_label.grid(row=0, column=0)
        self.index_entry = Entry(self.index_frame)
        self.index_entry.grid(row=1,column=0, sticky=E)
        self.index_button = Button(self.index_frame, text="Find", command=self.find_fields)
        self.index_button.grid(row=2,column=0,sticky=N)
        self.next_button = Button(self.index_frame, text="Next block", command=self.next_fields)
        self.next_button.grid(row=3,column=0,sticky=N)
        self.prev_button = Button(self.index_frame, text="Previous block", command=self.prev_fields)
        self.prev_button.grid(row=4,column=0,sticky=N)


        self.blockchain_label = Label(self.blockchain_frame, text="Blockchain Info:", fg="black")
        self.blockchain_label.grid(sticky=N)
        self.chain_field1 = Label(self.blockchain_frame, text="Blockchain Length:", fg="black")
        self.chain_field2 = Label(self.blockchain_frame, text="Supply:", fg="black")
        self.chain_field3 = Label(self.blockchain_frame, text="Average Work Time:", fg="black")

        self.chain_field1.grid(row=1, column=0, sticky=E)
        self.chain_field2.grid(row=2, column=0, sticky=E)
        self.chain_field3.grid(row=3, column=0, sticky=E)

        self.blockchain_length = Label(self.blockchain_frame, text=self.blockchain.getLength(), fg="black")
        self.blockchain_supply = Label(self.blockchain_frame, text=self.blockchain.getSupply(), fg="black")
        self.blockchain_avg_worktime = Label(self.blockchain_frame, text=self.blockchain.get_average_worktime(), fg="black")

        self.blockchain_length.grid(row=1, column = 1, sticky=W)
        self.blockchain_supply.grid(row=2, column = 1, sticky=W)
        self.blockchain_avg_worktime.grid(row=3, column = 1, sticky=W)


        self.menubar = Menu(self.root)
        self.drop = Menu(self.menubar, tearoff=0)
        self.drop.add_separator()
        self.drop.add_command(label="3", command=lambda: self.menu_difficulty(3))
        self.drop.add_command(label="4", command=lambda: self.menu_difficulty(4))
        self.drop.add_command(label="5", command=lambda: self.menu_difficulty(5))
        self.drop.add_command(label="6", command=lambda: self.menu_difficulty(6))
        self.drop.add_command(label="7", command=lambda: self.menu_difficulty(7))
        self.drop.add_command(label="8", command=lambda: self.menu_difficulty(8))
        self.menubar.add_cascade(label="Difficulty", menu=self.drop)
        self.root.config(menu=self.menubar)


        self.block_field1 = Label(self.block_frame, text="Block hash: ", fg="black")
        self.block_field2 = Label(self.block_frame, text="Height: ", fg="black")
        self.block_field3 = Label(self.block_frame, text="Nonce: ", fg="black")
        self.block_field4 = Label(self.block_frame, text="Mined at: ", fg="black")
        self.block_field5 = Label(self.block_frame, text="Previous hash: ", fg="black")
        self.block_field6 = Label(self.block_frame, text="Work time: ", fg="black")

        self.block_field1.grid(row=1,column=0, sticky=E)
        self.block_field2.grid(row=2,column=0, sticky=E)
        self.block_field3.grid(row=3,column=0, sticky=E)
        self.block_field4.grid(row=4,column=0, sticky=E)
        self.block_field5.grid(row=5,column=0, sticky=E)
        self.block_field6.grid(row=6,column=0, sticky=E)

        self.latest_block_hash = Label(self.block_frame, text=self.blockchain.getLatestBlock().getBlockHash(), fg="black")
        self.latest_block_height = Label(self.block_frame, text=self.blockchain.getLatestBlock().getHeight(), fg="black")
        self.latest_block_nonce = Label(self.block_frame, text=self.blockchain.getLatestBlock().getNonce(), fg="black")
        self.latest_block_time = Label(self.block_frame, text=self.blockchain.getLatestBlock().getMineTime(), fg="black")
        self.latest_block_prev_hash = Label(self.block_frame, text=self.blockchain.getLatestBlock().getPrevHash(), fg="black")
        self.latest_block_work_time = Label(self.block_frame, text=self.blockchain.getLatestBlock().get_work_time(), fg="black")

        self.latest_block_hash.grid(row=1, column=1, sticky=W)
        self.latest_block_height.grid(row=2, column=1, sticky=W)
        self.latest_block_nonce.grid(row=3, column=1, sticky=W)
        self.latest_block_time.grid(row=4, column=1, sticky=W)
        self.latest_block_prev_hash.grid(row=5, column=1, sticky=W)
        self.latest_block_work_time.grid(row=6, column=1, sticky=W)


        self.root.mainloop()

    def update_X(self):
        for x in range(int(self.data_entry.get())):
            self.update_fields()

    def update_loop(self):
        for x in range(10):
            self.update_fields()

    def update_fields(self):
        createBlock(self.blockchain, self.data_entry.get())
        self.latest_block_hash.config(text=(self.blockchain.getLatestBlock().getBlockHash()))
        self.latest_block_height.config(text=(self.blockchain.getLatestBlock().getHeight()))
        self.latest_block_nonce.config(text=(self.blockchain.getLatestBlock().getNonce()))
        self.latest_block_time.config(text=(self.blockchain.getLatestBlock().getMineTime()))
        self.latest_block_prev_hash.config(text=(self.blockchain.getLatestBlock().getPrevHash()))
        self.latest_block_work_time.config(text=self.blockchain.getLatestBlock().get_work_time())
        self.blockchain_length.config(text=self.blockchain.getLength())
        self.blockchain_supply.config(text=self.blockchain.getSupply())
        self.blockchain_avg_worktime.config(text=self.blockchain.get_average_worktime())

    def menu_difficulty(self, x):
        set_difficulty(x)
        self.difficulty_field.config(text=str(x))

    def find_fields(self):
        self.latest_block_hash.config(text=(self.blockchain.getBlockbyIndex(int(self.index_entry.get())).getBlockHash()))
        self.latest_block_height.config(text=(self.blockchain.getBlockbyIndex(int(self.index_entry.get())).getHeight()))
        self.latest_block_nonce.config(text=(self.blockchain.getBlockbyIndex(int(self.index_entry.get())).getNonce()))
        self.latest_block_time.config(text=(self.blockchain.getBlockbyIndex(int(self.index_entry.get())).getMineTime()))
        self.latest_block_prev_hash.config(text=(self.blockchain.getBlockbyIndex(int(self.index_entry.get())).getPrevHash()))

    '''Debug'''
    def next_fields(self):
        if int(self.latest_block_height.cget("text")) == self.blockchain.getLength():
            self.find_fields()
        else:
            self.latest_block_hash.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()+1).getBlockHash()))
            self.latest_block_height.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()+1).getHeight()))
            self.latest_block_nonce.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()+1).getNonce()))
            self.latest_block_time.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()+1).getMineTime()))
            self.latest_block_prev_hash.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()+1).getPrevHash()))

    def prev_fields(self):
        if int(self.latest_block_height.cget("text")) == 0:
            self.find_fields()
        else:
            self.latest_block_hash.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()-1).getBlockHash()))
            self.latest_block_height.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()-1).getHeight()))
            self.latest_block_nonce.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()-1).getNonce()))
            self.latest_block_time.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()-1).getMineTime()))
            self.latest_block_prev_hash.config(text=(self.blockchain.getBlockbyIndex(self.get_current_height()-1).getPrevHash()))

    def get_current_height(self):
            return int(self.latest_block_height.cget("text"))











if __name__ == "__main__":
    newBlockchain = Blockchain()
    oogeygooey = test_suite(newBlockchain)
